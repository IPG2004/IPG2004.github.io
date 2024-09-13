// database.cc
#include "database.h"
#include <iostream>

// -----------------------
// Implementación de Database
// -----------------------

Database::Database() : db(nullptr), exitCode(0) {}

Database::~Database() {
    closeDatabase();
}

bool Database::openDatabase(const std::string& filename) {
    exitCode = sqlite3_open(filename.c_str(), &db);

    if (exitCode) {
        std::cerr << "Error opening database: " << sqlite3_errmsg(db) << std::endl;
        return false;
    }
    std::cout << "Database opened successfully!" << std::endl;
    return true;
}

void Database::closeDatabase() {
    if (db) {
        sqlite3_close(db);
        std::cout << "Database connection closed." << std::endl;
    }
}

bool Database::executeQuery(const std::string& query) {
    char* errMsg = nullptr;
    exitCode = sqlite3_exec(db, query.c_str(), nullptr, 0, &errMsg);

    if (exitCode != SQLITE_OK) {
        std::cerr << "Error executing SQL: " << errMsg << std::endl;
        sqlite3_free(errMsg);
        return false;
    }
    std::cout << "SQL executed successfully!" << std::endl;
    return true;
}

// -----------------------
// Implementación de BillingDatabase
// -----------------------

BillingDatabase::BillingDatabase() {}

BillingDatabase::~BillingDatabase() {}

bool BillingDatabase::createProductsTable() {
    const std::string query = 
        "CREATE TABLE IF NOT EXISTS products ("
        "id INTEGER PRIMARY KEY AUTOINCREMENT, "
        "name TEXT NOT NULL, "
        "price REAL NOT NULL, "
        "barcode TEXT NOT NULL UNIQUE);";
    
    return executeQuery(query);
}

bool BillingDatabase::insertProduct(const std::string& name, double price, const std::string& barcode) {
    std::string query = "INSERT INTO products (name, price, barcode) VALUES ('" 
                        + name + "', " + std::to_string(price) + ", '" + barcode + "');";
    
    return executeQuery(query);
}

// Función callback para procesar los resultados de una consulta SELECT
static int productCallback(void* NotUsed, int argc, char** argv, char** azColName) {
    for (int i = 0; i < argc; i++) {
        std::cout << azColName[i] << ": " << (argv[i] ? argv[i] : "NULL") << std::endl;
    }
    std::cout << std::endl;
    return 0;
}

bool BillingDatabase::getProducts() {
    const std::string query = "SELECT * FROM products;";
    exitCode = sqlite3_exec(db, query.c_str(), productCallback, 0, nullptr);

    if (exitCode != SQLITE_OK) {
        std::cerr << "Error retrieving products." << std::endl;
        return false;
    }
    std::cout << "Products retrieved successfully!" << std::endl;
    return true;
}

bool BillingDatabase::getProducts(std::vector<std::string>& products) {
    const std::string query = "SELECT * FROM products;";
    exitCode = sqlite3_exec(db, query.c_str(), productCallback, 0, nullptr);

    if (exitCode != SQLITE_OK) {
        std::cerr << "Error retrieving products." << std::endl;
        return false;
    }
    std::cout << "Products retrieved successfully!" << std::endl;
    return true;
}

bool BillingDatabase::showProducts() {
    std::vector<std::string> products;
    if (!getProducts(products)) {
        std::cerr << "Error retrieving products." << std::endl;
        return false;
    }
    
    std::cout << "Products:" << std::endl;
    for (const auto& product : products) {
        std::cout << product << std::endl;
    }
    return true;
}

bool BillingDatabase::deleteProduct(const std::string& barcode) {
    std::string query = "DELETE FROM products WHERE barcode = '" + barcode + "';";
    return executeQuery(query);
}

bool BillingDatabase::updateProductPrice(const std::string& barcode, double newPrice) {
    std::string query = "UPDATE products SET price = " + std::to_string(newPrice) + " WHERE barcode = '" + barcode + "';";
    return executeQuery(query);
}


