try:
    from app import app
    print("SUCCESS: Flask app imported successfully!")
    print("The application is ready to run.")
    print("\nTo start the server, run: python app.py")
    print("Then visit: http://localhost:5000")
except Exception as e:
    print(f"ERROR: Failed to import Flask app: {str(e)}")