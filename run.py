from __init__ import create_app
app = create_app()

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # default to 5000 locally
    app.run(host="0.0.0.0", port=port, debug=True)

