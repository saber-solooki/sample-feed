import inject

from core_architecture.mixin import CreateDataMixin, RetrieveDataMixin
from core_architecture.view import CleanAPIView, CAListAPIView
from rss_feed.domain.use_cases.channel_list import ChannelListUseCase
from rss_feed.domain.use_cases.create_channel import CreateChannelUseCase
from rss_feed.serializer import CreateFeedSerializer, ChannelSerializer


class ChannelView(RetrieveDataMixin, CreateDataMixin, CleanAPIView):
    @inject.autoparams()
    def __init__(self, use_case: CreateChannelUseCase, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.use_case = use_case
        self.serializer = None

    def is_data_valid(self, request):
        if request.method == "POST":
            self.serializer = CreateFeedSerializer(data=request.data)
            return self.serializer.is_valid()

        return super().is_data_valid(request)

    def get(self, request, *args, **kwargs):
        self.check_request_data(request)
        return self.retrieve(request, *args, **kwargs)

    def get_data_query(self, request, *args, **kwargs):
        channel_id = kwargs.get('channel_id')
        pass

    def post(self, request, *args, **kwargs):
        self.check_request_data(request)
        return self.create(request, *args, **kwargs)

    def perform_create_data(self, request, *args, **kwargs):
        self.use_case.create_channel(self.serializer.validated_data['feed_address'])


class ChannelListView(CAListAPIView):
    serializer_class = ChannelSerializer

    @inject.autoparams()
    def __init__(self, use_case: ChannelListUseCase, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.use_case = use_case

    def get_list_query(self, request, *args, **kwargs):
        return self.use_case.get_list(request.query_params)
