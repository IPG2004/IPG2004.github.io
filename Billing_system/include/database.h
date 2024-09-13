// database.h
#ifndef DATABASE_H
#define DATABASE_H

#include <sqlite3.h>
#include <string>
#include <vector>

// Clase base para manejar la conexión a la base de datos
class Database {
protected:
    sqlite3* db;
    int exitCode;

public:
    Database();  // Constructor
    virtual ~Database();  // Destructor

    bool openDatabase(const std::string& filename);  // Abrir la base de datos
    void closeDatabase();  // Cerrar la base de datos
    bool executeQuery(const std::string& query);  // Ejecutar una consulta sin retorno
};

// Clase derivada para operaciones específicas de facturación
class BillingDatabase : public Database {
public:
    BillingDatabase();  // Constructor
    ~BillingDatabase();  // Destructor

    // Operaciones específicas
    bool createProductsTable();  // Crear tabla de productos
    bool insertProduct(const std::string& name, double price, const std::string& barcode);  // Insertar producto
    bool getProducts();  // Obtener productos (consulta SELECT)
    bool getProducts(std::vector<std::string>& products);  // Obtener productos (consulta SELECT)
    bool showProducts();  // Mostrar productos
    bool deleteProduct(const std::string& barcode);  // Eliminar producto
    bool updateProductPrice(const std::string& barcode, double newPrice);  // Actualizar precio de producto

};

#endif
