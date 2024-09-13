# Compilador y flags
CXX = g++
CXXFLAGS = -std=c++17 -Wall -Iinclude

# Librerías necesarias (ajusta según tu sistema)
LIBS = -lopencv_core -lopencv_highgui -lopencv_imgcodecs -lopencv_imgproc -lzbar -lhpdf -lsqlite3

# Directorios
SRC_DIR = src
INCLUDE_DIR = include
TEST_DIR = tests
BUILD_DIR = build

# Archivos fuente
SRC_FILES = $(SRC_DIR)/main.cc $(SRC_DIR)/barcode_reader.cc $(SRC_DIR)/database.cc $(SRC_DIR)/pdf_generator.cc $(SRC_DIR)/utils.cc
OBJ_FILES = $(SRC_FILES:.cc=.o)

# Archivos de prueba
TEST_FILES = $(TEST_DIR)/test_barcode_reader.cc $(TEST_DIR)/test_database.cc $(TEST_DIR)/test_pdf_generator.cc $(TEST_DIR)/test_utils.cc
# TEST_FILES = $(TEST_DIR)/test_database.cc

TEST_OBJ_FILES = $(TEST_FILES:.cc=.o)

# Ejecutables
EXEC = billing_system
TEST_EXEC = test_all

# Generar binarios principales
all: $(EXEC)

# Compilar el sistema principal
$(EXEC): $(OBJ_FILES)
	$(CXX) $(CXXFLAGS) $(OBJ_FILES) -o $(EXEC) $(LIBS)

# Compilar los archivos de prueba
tests: $(TEST_OBJ_FILES) $(OBJ_FILES)
	$(CXX) $(CXXFLAGS) $(TEST_OBJ_FILES) $(OBJ_FILES) -o $(TEST_EXEC) $(LIBS)

# Ejecutar pruebas
run_tests: tests
	./$(TEST_EXEC)

# Limpiar archivos compilados
clean:
	rm -f $(SRC_DIR)/*.o $(TEST_DIR)/*.o $(EXEC) $(TEST_EXEC)

