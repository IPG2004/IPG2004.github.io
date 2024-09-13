// test_database.cc
#include "database.h"
#include <iostream>

/*
int main() {
    // Crear una instancia de la clase BillingDatabase
    BillingDatabase billingDb;

    // Abrir la base de datos
    if (!billingDb.openDatabase("data/billing.db")) {
        return -1;
    }

    // Crear la tabla de productos si no existe
    if (!billingDb.createProductsTable()) {
        billingDb.closeDatabase();
        return -1;
    }

    // Insertar un producto
    if (!billingDb.insertProduct("Example Product", 9.99, "123456789012")) {
        billingDb.closeDatabase();
        return -1;
    }

    // Obtener y mostrar los productos
    std::vector<std::string> products;
    if (!billingDb.getProducts(products)) {
        billingDb.closeDatabase();
        return -1;
    }

    std::cout << "Products:" << std::endl;
    for (const auto& product : products) {
        std::cout << product << std::endl;
    }

    // Actualizar el precio de un producto
    if (!billingDb.updateProductPrice("123456789012", 7.99)) {
        billingDb.closeDatabase();
        return -1;
    }

    // Mostrar los productos actualizados
    if (!billingDb.showProducts()) {
        billingDb.closeDatabase();
        return -1;
    }

    // Eliminar un producto
    if (!billingDb.deleteProduct("123456789012")) {
        billingDb.closeDatabase();
        return -1;
    }


    // Cerrar la base de datos
    billingDb.closeDatabase();
    std::cout << "Database closed successfully" << std::endl;
    return 0;
}
*/
