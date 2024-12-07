class Article:
    all = []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        if hasattr(self, '_title'):
            return  # Prevent changing the title after it's set
        if isinstance(title, str) and 5 <= len(title) <= 50:
            self._title = title
        else:
            raise Exception("Title must be a string between 5 and 50 characters.")

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, author):
        if isinstance(author, Author):
            self._author = author
        else:
            raise Exception("Author must be an instance of the Author class.")

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, magazine):
        if isinstance(magazine, Magazine):
            self._magazine = magazine
        else:
            raise Exception("Magazine must be an instance of the Magazine class.")

        
class Author:
    all = []

    def __init__(self, name):
        if isinstance(name, str) and len(name) > 0:
            self._name = name
        else:
            raise Exception("Name must be a non-empty string.")
        Author.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if hasattr(self, '_name'):
            return  # Prevent changing the name after it's set

    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        return list(set(article.magazine for article in self.articles()))

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        categories = list(set(magazine.category for magazine in self.magazines()))
        return categories if categories else None


class Magazine:
    all = []

    def __init__(self, name, category):
        if isinstance(name, str) and 2 <= len(name) <= 16:
            self._name = name
        else:
            raise Exception("Name must be a string between 2 and 16 characters.")
        if isinstance(category, str) and len(category) > 0:
            self._category = category
        else:
            raise Exception("Category must be a non-empty string.")
        Magazine.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and 2 <= len(name) <= 16:
            self._name = name
        else:
            print("Name must be a string between 2 and 16 characters.")  # Log instead of raising an exception

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, category):
        if isinstance(category, str) and len(category) > 0:
            self._category = category
        else:
            print("Category must be a non-empty string.")  # Log instead of raising an exception

    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        return list(set(article.author for article in self.articles()))

    def article_titles(self):
        titles = [article.title for article in self.articles()]
        return titles if titles else None

    def contributing_authors(self):
        from collections import Counter
        authors = [article.author for article in self.articles()]
        return [author for author, count in Counter(authors).items() if count > 2] or None

    @classmethod
    def top_publisher(cls):
        return max(cls.all, key=lambda magazine: len(magazine.articles()), default=None)
