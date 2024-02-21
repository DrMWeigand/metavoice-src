import subprocess
import time
import requests

def check_server_ready(url):
    health_url = f"{url}/health"  # Adjust the URL to the health check endpoint
    try:
        response = requests.get(health_url)
        if response.status_code == 200:
            return True
    except requests.ConnectionError:
        pass
    return False


def main():
    backend_command = "python fam/llm/serving.py --huggingface_repo_id=""metavoiceio/metavoice-1B-v0.1"""
    frontend_script = "python fam/ui/app.py"
    
    # Start the backend server
    backend_process = subprocess.Popen(backend_command, shell=True)
    
    # Wait for the backend server to be ready
    print("Waiting for the backend server to be ready...")
    server_url = "http://127.0.0.1:58003"  # Adjust the URL and port as necessary
    while not check_server_ready(server_url):
        print("Server not ready, waiting...")
        time.sleep(1)  # Wait for 1 second before trying again
    print("Backend server is ready.")
    
    # Once the backend is ready, start the frontend Gradio app
    print("Starting the frontend Gradio interface...")
    subprocess.run(frontend_script, shell=True)

if __name__ == "__main__":
    main()
