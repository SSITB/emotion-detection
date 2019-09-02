# Emotion Detection
---------
## Objective:

We, as humans, are good at detecting person's feeling especially given the context and tone, we can detect even a slightest change in the tone, and thus the mood of the person. Sometimes, though, it's not always possible to rely on one's ability to detect/sense aggressiveness or other emotions, and it is important to involve machines in the process to assist people. So the aim of this project is to classify human emotions according to 6 core emotions and neutral state given the photograph of the facial expression.

 ---

## Project Overview


1. Although there are datasets readily available for development of such classifiers, this being a learning project for me, I decided (with a gentle push from [J.Beightol](https://www.linkedin.com/in/j-beightol-04615329/) to scrape and create my own image dataset using BING API.

    - I scraped around 850-950 images for each emotion, with the help of the Adrian Rosebrock's blogpost on [scraping images using Bing API](https://www.pyimagesearch.com/2018/04/09/how-to-quickly-build-a-deep-learning-image-dataset/), by the way, I encourage you to explore his website, he teaches a lot of useful tools and tricks in image processing and provides valuable information.

    - Further scraping just downloaded duplicate images, so there was no way to download more images than 950


2. Data cleaning is an essential part of any data science project

    - Since, the data was scraped from the internet, and internet being internet, there were many inadequate images, such as emojis or drawings and plenty of duplicates.

    - There's no way to clean image dataset programmatically, hence I had to clean the data manually. At this point, I was glad the dataset was on a smaller side.


3. Time for the first model:

    - Given the small dataset, I decided to perform data augmentation, ImageDataGenerator, in particular. This transformer would transform images in batches, skew/flip/rotate them, and would enable the model to generalize better.

    - I initiated my first Keras Model in order to analyze it's performance. Due to limitations of my personal computer's computational power, the parameters of the model are somewhat limited. Yet for the 7 categories output the model performed with the 45% accuracy


4. I thought of ways to improve the performance of my classifier model and decided to deploy face detection algorithm, detect the face on the image and resize it accordingly, getting rid of the gesture and body poses.

    - Since I was using OpenCV for my project extensively, I decided to utilize OpenCV HAAS Cascade Classifier to detect the faces.

    - This algorithm has a 95% accuracy, so I had to go back and manually clean the dataset again and leave only the images with the proper detected faces on them

5. Using this newly created dataset I fitted my second model:

    - The accuracy score improved to 50%

    - At this point I attempted to deploy AWS server in order to run more powerful model, but it seems, that the accuracy score will remain the same. Although, looking at the confusion matrix, it seems that the model performs very well on some emotions, whereas others have more false positives. I assign this to the small size of the dataset, I'm pretty sure, that larger dataset will produce far better results.

---

## Useful links

1. This is the link to the [Data Scraper NB](./image_scraper.ipynb) in case you want to check out the code for scraping data using BING API, although the python code is in [Search](./search/) folder.

2. Follow this link [Model NB](./model.ipynb) to check out how Keras model performs using ImageDataGenerator

3. To check out the face detecting and cropping code click on this link [Face Detection and Resizing NB](./face_cropping.ipynb), the python code can be found [here](./image_processing.py)

4. This is the link to the [Model with detected faces](./model_emotions.ipynb) which covers

    - Model performance with the newly created dataset

    - Random image selection and their classification by the model in accordance with the seven core emotions.


---

## Conclusions

In my opinion, better accuracy of the classifier can be achieved utilizing larger dataset and using more computational power. However, the approach of using only 7 core emotions has been criticized for not being an accurate representation of the actual emotions that people feel. Essentially, people may feel range of emotions at one given moment. Moreover the facial expression doesn't necessarily represent the emotion, say scowl may not be an expression of anger, etc. And in those important situation, such as security breach situations, the terrorist/attacker may have a poker face in place of scowl, so the aggressiveness may be detected by analyzing the body language and the tone.

Hence, this project may be as a first step for detecting emotional state of a person, but to provide and extensive overview of person's mood or emotional state, other features such as gesture, body language, language tone should be incorporated.


---

### Possible applications of the project:

1. This project can be used as a starting point to detect emotional state and be deployed as an additional aid for security purposes


2. AI safety driving to detect how tired/sleepy driver is, and others.
