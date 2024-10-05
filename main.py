import os
import requests
import platform

def temizle():
    os_turu = platform.system()
    if os_turu == "Windows":
        os.system("cls")
    elif os_turu in ["Linux", "Darwin"]:  # Linux ve macOS
        os.system("clear")
    else:
        print("[<>] The purge command is not supported for this operating system.")

# Clear the screen
temizle()

# Display title after clearing the screen
print("""
             d8888          d8b                    
            d88888          Y8P                    
           d88P888                                 
          d88P 888 88888b.  888                    
         d88P  888 888 "88b 888                    
        d88P   888 888  888 888                    
       d8888888888 888 d88P 888                    
      d88P     888 88888P"  888                    
                   888                             
                   888                             
                   888                             
88888888888                888                     
    888                    888                     
    888                    888                     
    888   .d88b.  .d8888b  888888  .d88b.  888d888 
    888  d8P  Y8b 88K      888    d8P  Y8b 888P"   
    888  88888888 "Y8888b. 888    88888888 888     
    888  Y8b.          X88 Y88b.  Y8b.     888     
    888   "Y8888   88888P'  "Y888  "Y8888  888     
""")

def fetch_api_response(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.json()  # Return the JSON response
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == "__main__":
    try:
        api_url = input("Please enter the API URL: ")
        result = fetch_api_response(api_url)

        if result is not None:
            print("API Response:")
            print(result)
    except KeyboardInterrupt:
        print("\n[<>] Program terminated by user.")
