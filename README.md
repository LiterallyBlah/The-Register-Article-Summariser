# The-Register-Article-Summariser
Summarises 'The Register' Articles using GPT from OpenAI. You can summarise all articles under a specific tag or summarise a specified blog. Under the second option it will list the articles created on the same day, and then you can select which article you would like to be summarised. Another option is the 'Summarise All Articles', which does as it says... summarises all articles one by one.

## Prerequisites
The following python libraries need to be installed:
* bs4 (BeautifulSoup)
* openai
* requests
* datetime

## How to run
`python3 theRegisterSummariser.py`

Initial options:

![image](https://user-images.githubusercontent.com/22526586/224951601-d8127c1c-3f87-4ebf-9f14-b54bb036cc88.png)

Option 1:

![image](https://user-images.githubusercontent.com/22526586/224951658-adb4db14-1fd2-4007-b2a4-05389252b4d7.png)

Option 2:

![image](https://user-images.githubusercontent.com/22526586/224951744-f69c8a37-909b-435c-bb81-f8e4feb44882.png)


## Configuring the script
### OpenAI API Key
Make sure you change the OpenAI API key:
`openai.api_key = "<CHANGE_ME>"`

You can create your OpenAI API key here: https://openai.com/blog/openai-api

### The Prompt
By default, the script uses the following prompt to generate the summary:
`prompt=f"Summarize the following text:\n\n{text}\n\nSummary:"`

The important part being 'Summarize the following text:'. If you want something like a bulleted list instead, you can change the prompt to something like:
`prompt=f"Summarize the following text into a bulleted list:\n\n{text}\n\nSummary:"`

The important change is 'Summarize the following text into a bulleted list:' instead of 'Summarize the following text:'. 
