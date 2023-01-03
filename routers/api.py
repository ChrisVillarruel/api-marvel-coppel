from fastapi import APIRouter, HTTPException

router = APIRouter()


@router.get("/searchCharacter/")
async def character_search(name_starts_with: str = 'None', name: str = 'None'):
    return {"name_starts_with": name_starts_with, "name": name}


@router.get("/searchComics/")
async def comics_search(title_starts_with: str = 'None', title: str = 'None'):
    return {"title_starts_with": title_starts_with, "title": title}
