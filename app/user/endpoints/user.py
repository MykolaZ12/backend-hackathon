from typing import Any, List

from fastapi import APIRouter, Body, Depends, HTTPException, BackgroundTasks
from sqlalchemy.orm import Session

from app.user import schemas, services, models, permission
from config import settings
from db.db import get_db

router = APIRouter()


@router.get("/",
            response_model=List[schemas.UserInResponse],
            dependencies=[Depends(permission.get_current_superuser)])
def read_users(
        db: Session = Depends(get_db),
        skip: int = 0,
        limit: int = 100,
) -> Any:
    """
    Retrieve users.
    """
    users = services.user_crud.get_multi(db, skip=skip, limit=limit)
    return users


@router.post("/", response_model=schemas.UserInResponse)
def create_user(*,
                db: Session = Depends(get_db),
                user_in: schemas.UserCreate,
                background_tasks: BackgroundTasks
                ) -> Any:
    """
    Create new user.
    """
    user = services.user_crud.get(db, email=user_in.email)
    if user:
        raise HTTPException(
            status_code=400,
            detail="The user with this username already exists in the system.",
        )
    user = services.user_crud.create(db, schema=user_in)
    if settings.EMAILS_ENABLED and user_in.email:
        background_tasks.add_task(
            services.send_new_account_email, email_to=user_in.email, username=user_in.email,
            password=user_in.password
        )
    return user


@router.put("/me", response_model=schemas.UserInResponse)
def update_user_me(
        *,
        db: Session = Depends(get_db),
        scheme: schemas.UserUpdate,
        current_user: models.User = Depends(permission.get_current_active_user),
) -> Any:
    """
    Update own user.
    """
    user = services.user_crud.update(db, db_obj=current_user, obj_in=scheme)
    return user


@router.get("/me", response_model=schemas.UserInResponse)
def read_user_me(
        db: Session = Depends(get_db),
        current_user: models.User = Depends(permission.get_current_active_user),
) -> Any:
    """
    Get current user.
    """
    return current_user


@router.get("/{user_id}", response_model=schemas.UserInResponse)
def read_user_by_id(
        user_id: int,
        current_user: models.User = Depends(permission.get_current_active_user),
        db: Session = Depends(get_db),
) -> Any:
    """
    Get a specific user by id.
    """
    user = services.user_crud.get(db, id=user_id)
    if user == current_user:
        return user
    if not services.user_crud.is_superuser(current_user):
        raise HTTPException(
            status_code=400, detail="The user doesn't have enough privileges"
        )
    return user


@router.put("/{user_id}",
            response_model=schemas.UserInResponse,
            dependencies=[Depends(permission.get_current_superuser)])
def update_user(
        *,
        db: Session = Depends(get_db),
        user_id: int,
        user_in: schemas.UserUpdate,
) -> Any:
    """
    Update a user.
    """
    user = services.user_crud.get(db, id=user_id)
    if not user:
        raise HTTPException(
            status_code=404,
            detail="The user with this username does not exist in the system",
        )
    user = services.user_crud.update(db, db_obj=user, obj_in=user_in)
    return user
