
import matplotlib.pyplot as plt
from wordcloud import WordCloud


def word_frequency(text):
    words = text.split()
    word_count = {}
    for word in words:
        if word not in word_count:
            word_count[word] = 1
        else:
            word_count[word] += 1
    return word_count


# Function to create word cloud
def generate_word_cloud(text):
    wordcloud = WordCloud(width=800, height=800,
                          background_color='white',
                          stopwords=[],
                          min_font_size=10).generate(text)
    return wordcloud


def mock_func(text1, text2):
    freq1 = word_frequency(text1)
    freq2 = word_frequency(text2)
    fig, axs = plt.subplots(1, 2, figsize=(10, 5), tight_layout=True)

    axs[0].title.set_text("file1")
    axs[1].title.set_text("file2")
    axs[0].pie(list(freq1.values()), labels=list(freq1.keys()), autopct='%1.1f%%')
    axs[1].pie(list(freq2.values()), labels=list(freq2.keys()), autopct='%1.1f%%')
    plt.show()
    wordcloud1 = generate_word_cloud(text1)
    wordcloud2 = generate_word_cloud(text2)
    fig, axs = plt.subplots(1, 2, figsize=(10, 5))
    axs[0].imshow(wordcloud1)
    axs[0].axis('off')
    axs[0].set_title("file1")
    axs[1].imshow(wordcloud2)
    axs[1].axis('off')
    axs[1].set_title("file2")
    plt.show()
