from fastapi import APIRouter, HTTPException, status

router= APIRouter(prefix="/products",
                    tags=["Products"],
                    responses={HTTPException(status_code=status.HTTP_404_NOT_FOUND):{"message":"Not found"}})


products_list = ["Producto 0", "Producto 1","Producto 2","Producto 3","Producto 4",]


@router.get("/")
async def products():
    return []


@router.get("/{id}")
async def products(id:int):
    return products_list[id]