# The-Register-Article-Summariser
Summarises 'The Register' Articles using GPT from OpenAI. It will list the articles created on the same day, and then you can select which article you would like to be summarised. Another option is the 'Summarise All Articles', which does as it says... summarises all articles one by one.

## Prerequisites
The following python libraries need to be installed:
* bs4 (BeautifulSoup)
* openai
* requests
* datetime

## Changes to the script
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
