# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

import json


def handler(event, context):
    # Simple example: reset password or check server status
    action = event.get('action')
    if action == "reset_password":
        user = event.get('user', 'unknown')
        return {"statusCode": 200, "body": f"Password reset initiated for {user}"}
    elif action == "check_server_status":
        server = event.get('server', 'all')
        return {"statusCode": 200, "body": f"Server {server} is running normally"}
    else:
        return {"statusCode": 400, "body": "Unknown action"}
