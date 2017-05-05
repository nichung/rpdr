### to do:
+ complete data collection for two episodes
+ make script to extract relevant data from json response in format amenable to manual revision

### questions:
+ add RuPaul commentary as control?
+ how specific should the "context" and "episode arc" be? (Must be answered through EDA)
+ measure duration of quote? If so, must capture quote end timestamp

### additional notes:
+ "grouping" refers to conversation. Must improve conversation grouping notation
+ quotation marks for "comment" / actual quote?
+ facial expressions are as good as words -- emojis?

### speech recognition with Google Cloud Speech API
1. record audio and convert to .flac format
2. enable Cloud Speech API in GCP
3. activate Cloud Shell
4. create API key
5. create Speech API request using longrunningrecognize method in request.json:

	'''json
	{
  	  "config": {
      	      "encoding":"FLAC",
              "sampleRateHertz": 16000,
              "languageCode": "en-US"
  	  },
  	    "audio": {
                "uri":"gs://{bucket-name}/{file-name}.flac"
  	  }
	}
	'''

6. call Speech API:
	
	$curl -s -X POST -H "content-Type: application/json" --data-binary @request.json "https://speech.goo
gleapis.com/v1/speech:longrunningrecognize?key=${API_KEY}"

7. wait at least 30 seconds, then GET the response by name and pipe to text file
	
	$curl -s GET "https://speech.googleapis.com/v1/operations/{operation-name}?key=${API_KEY}" > {file-name}.txt

8. send to storage bucket:

	$gsutil cp *.txt gs://{bucket-name}
