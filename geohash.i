
%module geohash
%{
#include "libgeohash/geohash.h"
%}

%rename(encode) geohash_encode;
%rename(decode) geohash_decode;

%include "libgeohash/geohash.h"
