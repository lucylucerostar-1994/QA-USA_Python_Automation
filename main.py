from helpers import is_url_reachable, format_string, calculate_percentage
from data import load_data, save_data, filter_data

def display_data(data):
    for item in data:
        print(format_string(item))

def main():
    url = "https://example.com"
    if is_url_reachable(url):
        print("URL is reachable.")
    else:
        print("URL is not reachable.")

    data = load_data('data.json')
    filtered = filter_data(data, "sample")
    display_data(filtered)
    save_data('filtered.json', filtered)

if __name__ == "__main__":
    main()
