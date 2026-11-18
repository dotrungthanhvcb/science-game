#!/usr/bin/env python3
"""
Figma API Client & MCP Helper for Antigravity
User: Thanh Do Trung (dotrungthanhhust@gmail.com)
"""

import sys
import os
import json
import urllib.request
import urllib.parse
import re

def get_token():
    t = os.environ.get("FIGMA_API_KEY")
    if t: return t
    token_file = os.path.join(os.path.dirname(__file__), "..", ".figma_token")
    if os.path.exists(token_file):
        with open(token_file, "r") as f:
            return f.read().strip()
    return ""

FIGMA_TOKEN = get_token()

def get_headers():
    return {
        "X-Figma-Token": FIGMA_TOKEN,
        "User-Agent": "Antigravity-Figma-Bridge/1.0"
    }

def request_figma(endpoint):
    url = f"https://api.figma.com/v1/{endpoint.lstrip('/')}"
    req = urllib.request.Request(url, headers=get_headers())
    try:
        with urllib.request.urlopen(req) as resp:
            return json.loads(resp.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        err_msg = e.read().decode('utf-8', errors='ignore')
        return {"error": True, "code": e.code, "message": err_msg}
    except Exception as e:
        return {"error": True, "message": str(e)}

def extract_file_key(url_or_key):
    """
    Extract file_key and optional node_id from Figma URL:
    https://www.figma.com/design/FILE_KEY/title?node-id=NODE_ID
    or https://www.figma.com/file/FILE_KEY/...
    """
    if '/' not in url_or_key:
        return url_or_key, None
    
    # Match /file/KEY or /design/KEY
    match = re.search(r'(?:file|design)/([a-zA-Z0-9]+)', url_or_key)
    file_key = match.group(1) if match else url_or_key

    # Check for node-id in URL query
    node_id = None
    node_match = re.search(r'[?&]node-id=([a-zA-Z0-9%:-]+)', url_or_key)
    if node_match:
        node_id = urllib.parse.unquote(node_match.group(1)).replace('%3A', ':').replace('-', ':')
    
    return file_key, node_id

def get_user_info():
    return request_figma("me")

def get_file(file_key, depth=None, node_ids=None):
    params = []
    if depth:
        params.append(f"depth={depth}")
    if node_ids:
        ids_str = ",".join(node_ids) if isinstance(node_ids, list) else node_ids
        params.append(f"ids={urllib.parse.quote(ids_str)}")
    
    query = f"?{'&'.join(params)}" if params else ""
    return request_figma(f"files/{file_key}{query}")

def get_node(file_key, node_id):
    return request_figma(f"files/{file_key}/nodes?ids={urllib.parse.quote(node_id)}")

def get_image_export(file_key, node_ids, format="png", scale=2):
    ids_str = ",".join(node_ids) if isinstance(node_ids, list) else node_ids
    return request_figma(f"images/{file_key}?ids={urllib.parse.quote(ids_str)}&format={format}&scale={scale}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: figma_client.py [me | file <url_or_key> [node_id] | export <url_or_key> <node_id>]")
        sys.exit(1)

    cmd = sys.argv[1]
    if cmd == "me":
        print(json.dumps(get_user_info(), indent=2, ensure_ascii=False))
    elif cmd == "file":
        if len(sys.argv) < 3:
            print("Error: missing url or key")
            sys.exit(1)
        key, node_id = extract_file_key(sys.argv[2])
        if len(sys.argv) >= 4:
            node_id = sys.argv[3]
        if node_id:
            res = get_node(key, node_id)
        else:
            res = get_file(key, depth=2)
        print(json.dumps(res, indent=2, ensure_ascii=False))
    elif cmd == "export":
        if len(sys.argv) < 4:
            print("Usage: figma_client.py export <url_or_key> <node_id> [format]")
            sys.exit(1)
        key, _ = extract_file_key(sys.argv[2])
        node_id = sys.argv[3]
        fmt = sys.argv[4] if len(sys.argv) >= 5 else "png"
        res = get_image_export(key, node_id, format=fmt)
        print(json.dumps(res, indent=2, ensure_ascii=False))
    else:
        print(f"Unknown command: {cmd}")
