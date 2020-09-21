from django.views import generic
from django.shortcuts import render
from .models import Book, Author, BookInstance, Genre
import logging

# 书籍首页
def index(request):
    """
    View function for home page of site.
    """
    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(
        status__exact='a').count()
    num_authors = Author.objects.count()  # The 'all()' is implied by default.

    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'index.html',
        context={'num_books': num_books, 'num_instances': num_instances,
                 'num_instances_available': num_instances_available, 'num_authors': num_authors},
    )



# 书籍列表
class BookListView(generic.ListView):
    model = Book

    paginate_by = 10   # 分页，每页的条数
    queryset = Book.objects.all()             # 返回全部数据
    template_name = 'catalog/book_list.html'  # 指定模板
    context_object_name = 'book_list'         # 指定字段



# 书籍详情（类写法）
# class BookDetailView(generic.DetailView):
#     """Generic class-based detail view for a book."""
#     model = Book

# 书籍详情(函数写法)
def book_detail_view(request,pk):
    """
    View function for book detail of site.
    """
    # get book detail by id
    book=Book.objects.get(pk=pk)

    return render(
        request,
        'catalog/book_detail.html',
        context={'book':book}
    )



# 作者列表
class AuthorListView(generic.ListView):
    model = Author

    paginate_by = 10   # 分页，每页的条数
    queryset = Author.objects.all()             # 返回全部数据
    template_name = 'catalog/author_list.html'  # 指定模板
    context_object_name = 'author_list'         # 指定字段


# 作者详情
def author_detail_view(request,pk):
    """
    View function for author detail of site.
    """
    # get book detail by id
    author=Author.objects.get(pk=pk)

    return render(
        request,
        'catalog/author_detail.html',
        context={'author':author}
    )
