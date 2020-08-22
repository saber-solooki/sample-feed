import inject

from collection.domain.entities.comment_feed_item_entity import CommentOnFeedItemRequestEntity
from collection.domain.use_cases.bookmark_feed_item import BookMarkFeedItemUseCase
from collection.domain.use_cases.comment_on_feed_item import CommentOnFeedItemUseCase
from collection.domain.use_cases.follow_channel import FollowChannelUseCase
from collection.domain.use_cases.get_feed_item_detail import GetFeedItemDetailUseCase
from collection.domain.use_cases.get_feed_items import GetUserFeedItemsUseCase
from collection.domain.use_cases.read_feed_item import ReadFeedItemUseCase
from collection.domain.use_cases.unfollow_channel import UnFollowChannelUseCase
from collection.domain.use_cases.user_channels_list import UserChannelsListUseCase
from collection.serializer import FollowChannelSerializer, ReadFeedItemSerializer, CommentOnFeedItemSerializer
from core_architecture.generics import CACreateAPIView, UpdateAPIView
from core_architecture.mixin import CreateDataMixin, DestroyDataMixin, RetrieveDataMixin
from core_architecture.view import CleanAPIView, CAListAPIView
from rss_feed.serializer import ChannelSerializer, FeedItemSerializer, UserFeedItemSerializer


class UserChannelView(DestroyDataMixin, CreateDataMixin, CleanAPIView):
    @inject.autoparams()
    def __init__(self, follow_use_case: FollowChannelUseCase, un_follow_use_case: UnFollowChannelUseCase, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.follow_use_case = follow_use_case
        self.un_follow_use_case = un_follow_use_case
        self.serializer = None

    def is_data_valid(self, request):
        if request.method == "POST":
            self.serializer = FollowChannelSerializer(data=request.data)
            return self.serializer.is_valid()

        return super().is_data_valid(request)

    def post(self, request, *args, **kwargs):
        self.check_request_data(request)
        return self.create(request, *args, **kwargs)

    def perform_create_data(self, request, *args, **kwargs):
        self.follow_use_case.follow(request.user.id, self.serializer.validated_data['channel_id'])

    def delete(self, request, *args, **kwargs):
        self.check_request_data(request)
        return self.destroy(request, *args, **kwargs)

    def perform_destroy(self, request, *args, **kwargs):
        self.un_follow_use_case.un_follow(request.user.id, kwargs.get('channel_id'))


class UserChannelsList(CAListAPIView):
    serializer_class = ChannelSerializer

    @inject.autoparams()
    def __init__(self, use_case: UserChannelsListUseCase, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.use_case = use_case

    def get_list_query(self, request, *args, **kwargs):
        return self.use_case.get_list(request.user.id, request.query_params.get('page', 1))


class UserUnreadFeedListView(CAListAPIView):
    serializer_class = FeedItemSerializer

    @inject.autoparams()
    def __init__(self, use_case: GetUserFeedItemsUseCase, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.use_case = use_case

    def get_list_query(self, request, *args, **kwargs):
        return self.use_case.get_feed_items(request.user.id, request.query_params.get('page', 1))


class FeedItemView(RetrieveDataMixin, CreateDataMixin, CleanAPIView):
    serializer_class = UserFeedItemSerializer

    @inject.autoparams()
    def __init__(self, read_feed_use_case: ReadFeedItemUseCase, get_user_feed_detail: GetFeedItemDetailUseCase, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.read_feed_use_case = read_feed_use_case
        self.get_user_feed_detail = get_user_feed_detail
        self.read_feed_serializer = None

    def is_data_valid(self, request):
        if request.method == "POST":
            self.read_feed_serializer = ReadFeedItemSerializer(data=request.data)
            return self.read_feed_serializer.is_valid()

        return super().is_data_valid(request)

    def post(self, request, *args, **kwargs):
        self.check_request_data(request)
        return self.create(request, *args, **kwargs)

    def perform_create_data(self, request, *args, **kwargs):
        self.read_feed_use_case.read_feed(request.user.id, self.read_feed_serializer.validated_data['feed_item_id'])

    def get(self, request, *args, **kwargs):
        self.check_request_data(request)
        return self.retrieve(request, *args, **kwargs)

    def get_data_query(self, request, *args, **kwargs):
        return self.get_user_feed_detail.get_detail(request.user.id, kwargs.get('feed_item_id'))


class BookMarkFeedItemView(UpdateAPIView):
    @inject.autoparams()
    def __init__(self, use_case: BookMarkFeedItemUseCase, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.use_case = use_case
        self.serializer = None

    def perform_update(self, request, *args, **kwargs):
        self.use_case.bookmark(request.user.id, kwargs.get('feed_item_id'))


class CommentOnFeedItemView(UpdateAPIView):
    @inject.autoparams()
    def __init__(self, use_case: CommentOnFeedItemUseCase, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.use_case = use_case
        self.serializer = None

    def is_data_valid(self, request):
        self.serializer = CommentOnFeedItemSerializer(data=request.data)
        return self.serializer.is_valid()

    def perform_update(self, request, *args, **kwargs):
        self.use_case.set_comment(
            CommentOnFeedItemRequestEntity(request.user.id, kwargs.get('feed_item_id'), self.serializer.validated_data['comment']))
