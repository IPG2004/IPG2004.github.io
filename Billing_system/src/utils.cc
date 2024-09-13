// utils.cc
#include "utils.h"

std::string doubleToStringWithTwoDecimals(double value) {
    std::ostringstream out;
    out << std::fixed << std::setprecision(2) << value;
    return out.str();
}