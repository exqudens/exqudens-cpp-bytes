#pragma once

#include <vector>

#include "exqudens/BytesExport.hpp"

namespace exqudens {

  class EXQUDENS_BYTES_EXPORT Bytes {

    public:

      static bool flag;

      static std::vector<unsigned char> toUnsignedCharVector(const std::vector<long>& values);
      static std::vector<unsigned char> toUnsignedCharVector(std::vector<long>& values);
      static std::vector<unsigned char> toUnsignedCharVector(const std::vector<long>* values);
      static std::vector<unsigned char> toUnsignedCharVector(std::vector<long>* values);

      static std::vector<long> toLongVector(const std::vector<unsigned char>& values);
      static std::vector<long> toLongVector(std::vector<unsigned char>& values);
      static std::vector<long> toLongVector(const std::vector<unsigned char>* values);
      static std::vector<long> toLongVector(std::vector<unsigned char>* values);

  };

}
