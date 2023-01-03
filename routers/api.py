from fastapi import APIRouter, HTTPException

from api_marvel.client import APICharacterSearch, APIComicsSearch
from api_marvel.exceptions import APIMarvelException

router = APIRouter(
    prefix="/v1/pruebaTecnica",
    tags=["items"],
)


@router.get("/searchCharacter/")
async def character_search(name_starts_with: str = 'None', name: str = 'None'):
    try:
        api = APICharacterSearch(nameStartsWith=name_starts_with, name=name)
    except APIMarvelException as e:
        raise HTTPException(status_code=400, detail=e.status)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    else:
        return api.response


@router.get("/searchComics/")
async def comics_search(title_starts_with: str = 'None', title: str = 'None'):
    try:
        api = APIComicsSearch(titleStartsWith=title_starts_with, title=title)
    except APIMarvelException as e:
        raise HTTPException(status_code=400, detail=e.status)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    else:
        return api.response
