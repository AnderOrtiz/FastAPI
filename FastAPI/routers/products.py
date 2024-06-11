from fastapi import APIRouter

router= APIRouter(prefix="/products",
                    tags=["Products"],
                    responses={404:{"message":"Not found"}})


products_list = ["Producto 0", "Producto 1","Producto 2","Producto 3","Producto 4",]


@router.get("/")
async def products():
    return []


@router.get("/{id}")
async def products(id:int):
    return products_list[id]