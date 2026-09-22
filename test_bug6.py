from main import TiendaOnline


def test_limpiar_agotados_elimina_productos_sin_stock():
    """Los productos con cantidad <= 0 deben desaparecer del inventario."""
    tienda = TiendaOnline()
    tienda.agregar_producto("P01", "Teclado Mecánico", 150000, 5)
    tienda.agregar_producto("P03", "Audífonos", 50000, 0)  # ya agotado

    tienda.inventario["P01"]["cantidad"] = 0
    tienda.limpiar_agotados()

    assert "P01" not in tienda.inventario
    assert "P03" not in tienda.inventario


def test_limpiar_agotados_conserva_productos_con_stock():
    """Los productos con stock disponible no deben eliminarse."""
    tienda = TiendaOnline()
    tienda.agregar_producto("P02", "Mouse Gamer", 80000, 3)

    tienda.limpiar_agotados()

    assert "P02" in tienda.inventario


def test_limpiar_agotados_no_lanza_runtime_error():
    """No debe lanzar RuntimeError al modificar el diccionario mientras se itera."""
    tienda = TiendaOnline()
    tienda.agregar_producto("P01", "Teclado Mecánico", 150000, 0)
    tienda.agregar_producto("P02", "Mouse Gamer", 80000, 0)
    tienda.agregar_producto("P03", "Audífonos", 50000, 0)

    # Si el bug no estuviera corregido, esta línea lanzaría RuntimeError
    tienda.limpiar_agotados()

    assert tienda.inventario == {}