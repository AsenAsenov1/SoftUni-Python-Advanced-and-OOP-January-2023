from project.category import Category
from project.document import Document
from project.topic import Topic


class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    @staticmethod
    def __find_instance_by_id(instance_id, list_of_instances):
        found_instance = [x for x in list_of_instances if x.id == instance_id][0]
        return found_instance

    def add_category(self, category: Category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic: Topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document: Document):
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id: int, new_name: str):
        category_obj = self.__find_instance_by_id(category_id, self.categories)
        category_obj.edit(new_name)

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        topic_obj = self.__find_instance_by_id(topic_id, self.topics)
        topic_obj.edit(new_topic, new_storage_folder)

    def edit_document(self, document_id: int, new_file_name: str):
        document_obj = self.__find_instance_by_id(document_id, self.documents)
        document_obj.edit(new_file_name)

    def delete_category(self, category_id):
        category_obj = self.__find_instance_by_id(category_id, self.categories)
        self.categories.remove(category_obj)

    def delete_topic(self, topic_id):
        topic_obj = self.__find_instance_by_id(topic_id, self.topics)
        self.topics.remove(topic_obj)

    def delete_document(self, document_id):
        document_obj = self.__find_instance_by_id(document_id, self.documents)
        self.documents.remove(document_obj)

    def get_document(self, document_id):
        document_obj = self.__find_instance_by_id(document_id, self.documents)
        return repr(document_obj)

    def __repr__(self):
        return '\n'.join([repr(document) for document in self.documents])
