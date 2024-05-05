# Push Hugo Website Markdown to Medium Blog
### <span style="color: red"> Disclaimer: </span> This code uses medium APIs V1 which is deprecated. It has been a year since they archived their APIs. However, it <span style="color: green"> STILL works</span>. so I am still using it to push my markdown articles to medium.


I use Hugo to build my website and I write my articles in markdown. I also have a medium blog where I write articles. I wanted to automate the process of pushing my articles to both my website and my medium blog. I found two interesting resources that made it easy for me. This code is a combination of the two resources and I added some modifications to constumize it to my needs.

## Objective
Convert Hugo markdown to medium post and push it to medium.

------------------------------------
## Steps

to use this project please follow the steps below:  
1. Get your **Medium integration token** from your medium account settings (at the bottom of Security and apps section), then create `.env` file and paste the token in it as follows:
   
    ```bash
    TOKEN="your-medium-integration-token"
    ```
2. Place your markdown file in the `input` folder, and place the images in the `images` folder that resides in the input forlder.

3. create a python virtual environment and install the required packages by running the following commands:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```
4. Run the code by running the following command:
    ```bash
    python publish.py "input/<YOUR_ARTICLE>.md" --title '<STORY TITLE>' --tags "<TAGS TO ASSOCIATE WITH THE ARTICLE>"
    ```    

> **_NOTE:_**  Please run the following to get help on how to use the code:
> ```bash
> python publish.py --help
> ```

## Results
You will get a URL to your article on medium and a URL to your article on your website.

## Resources
1. [Programmatically Publish Markdown as a Medium Story With Python](https://betterprogramming.pub/programmatically-publish-a-markdown-file-as-a-medium-story-with-python-b2b072a5f968)
2. [Publish a Medium post using Python](https://levelup.gitconnected.com/publish-a-medium-post-using-python-fccbe61c04e)