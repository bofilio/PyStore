from rest_framework import viewsets
from rest_framework.decorators import action
from backend.api.serializers import *
from backend.models import *
from rest_framework.response import Response
from rest_framework import filters


class UserViewSets(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CategoryViewSets(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    #disable pagination for this viewsets
    def paginate_queryset(self, queryset, view=None):
        return None
        #if 'no_page' in self.request.query_params:
            #return None
        #else:
            #return self.paginator.paginate_queryset(queryset, self.request, view=self)

class AddressViewSets(viewsets.ModelViewSet):
    queryset =  Address.objects.all()
    serializer_class = AddressSerializer

class NewsArticleViewSets(viewsets.ModelViewSet):
    queryset =  NewsArticle.objects.all()
    serializer_class = NewsArticleDetailsSerializer

    def list(self, request, *args, **kwargs):
        self.serializer_class=NewsArticleSerializer
        return super().list(request, *args, **kwargs)

class CurrencyViewSets(viewsets.ModelViewSet):
    queryset =  Currency.objects.all()
    serializer_class = CurrencySerializer

class ProfileViewSets(viewsets.ModelViewSet):
    queryset =  Profile.objects.all()
    serializer_class = ProfileSerializer


class ProductViewSets(viewsets.ModelViewSet):
    search_fields = ['title', 'description']
    filter_backends = (filters.SearchFilter,)
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer

    def list(self, request, *args, **kwargs):
        self.serializer_class=ProductSerializer
        return super().list(request, *args, **kwargs)

    @action(detail=False,url_path=r"bycat/(?P<cat_id>\d+)", methods=['get'])
    def bycat(self, request,cat_id):
        products=self.queryset.filter(categories__id= cat_id)
        page = self.paginate_queryset(products)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(products, many=True)
        return Response(serializer.data)

    @action(detail=False, url_path=r"popular/(?P<count>\d+)", methods=['get'])
    def popular(self, request, count):
        products = self.queryset.all().order_by("-visited")[:int(count)]
        page = self.paginate_queryset(products)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(products, many=True)
        return Response(serializer.data)

class ProductImageViewSets(viewsets.ModelViewSet):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer


class CartViewSets(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class OrderViewSets(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class CartItemViewSets(viewsets.ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer


class OrderItemViewSets(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer


class WishListViewSets(viewsets.ModelViewSet):
    queryset = WishList.objects.all()
    serializer_class = WishListSerializer


