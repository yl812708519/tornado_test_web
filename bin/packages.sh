#!/usr/bin/env bash
base_path=$(dirname $0)
base_path=${base_path/\./$(pwd)}
source $base_path/env.sh

echo $base_path/$APP_NAME/bin/activate
source $base_path/$APP_NAME/bin/activate

pip install -r $base_path/requirements.txt
