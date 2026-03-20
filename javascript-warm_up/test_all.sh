#!/bin/bash

echo "===== TEST 0 ====="
./0-javascript_is_amazing.js

echo "===== TEST 1 ====="
./1-multi_languages.js

echo "===== TEST 2 ====="
./2-arguments.js
./2-arguments.js Best
./2-arguments.js Best School

echo "===== TEST 3 ====="
./3-value_argument.js
./3-value_argument.js School

echo "===== TEST 4 ====="
./4-concat.js c cool
./4-concat.js c
./4-concat.js

echo "===== TEST 5 ====="
./5-to_integer.js
./5-to_integer.js 89
./5-to_integer.js School

echo "===== TEST 6 ====="
./6-multi_languages_loop.js

echo "===== TEST 7 ====="
./7-multi_c.js 2
./7-multi_c.js

echo "===== TEST 8 ====="
./8-square.js 2
./8-square.js

echo "===== TEST 9 ====="
./9-add.js 1 7
./9-add.js

echo "===== TEST 10 ====="
./10-factorial.js 3
./10-factorial.js

echo "===== TEST 11 ====="
./11-second_biggest.js 4 2 5 3 0 -3
./11-second_biggest.js

echo "===== TEST 12 ====="
./12-object.js

echo "===== TEST 13 ====="
./13-main.js

echo "===== SEMISTANDARD ====="
semistandard *.js || echo "❌ Style errors"
