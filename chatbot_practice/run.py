import os
import subprocess

def main():
    print("--- Professional AI Chatbot Launcher ---")
    print("Launching the Streamlit interface...")

    # This command triggers streamlit to run the app file
    cmd = ["streamlit", "run", "src/chatbot/app.py"]

    try:
        subprocess.run(cmd, check=True)
    except KeyboardInterrupt:
        print("\nStopping chatbot...")
    except Exception as e:
        print(f"Error launching app: {e}")
        print("\nTry running this manually in your terminal:")
        print("streamlit run src/chatbot/app.py")

if __name__ == "__main__":
    main()
