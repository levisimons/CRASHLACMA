from twitter_json_parser import TwitterJsonParser 

print("Running twitter client...")

input_data = 'data_raw_tweets/sample_mixed_data.json'

parser = TwitterJsonParser()
print(parser.get_data_from_tweets(input_data))