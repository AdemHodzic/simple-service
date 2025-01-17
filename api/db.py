# Copyright 2024 Flower Labs GmbH. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
"""Database module."""
import sqlite3

def get_connection():
    con = sqlite3.connect("users.db")
    cur = con.cursor()
    return cur

def setup_table():
    cur  = get_connection()
    cur.execute("CREATE TABLE IF NOT EXISTS users(id text, email text, hash text);")

