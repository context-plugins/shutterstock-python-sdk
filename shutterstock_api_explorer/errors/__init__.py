from .add_image_collection_items_error import AddImageCollectionItemsErrorBody, add_image_collection_items_error_mapper
from .add_track_collection_items_error import AddTrackCollectionItemsErrorBody, add_track_collection_items_error_mapper
from .add_video_collection_items_error import AddVideoCollectionItemsErrorBody, add_video_collection_items_error_mapper
from .authorize_error import AuthorizeErrorBody, authorize_error_mapper
from .bulk_search_images_error import BulkSearchImagesErrorBody, bulk_search_images_error_mapper
from .create_access_token_error import CreateAccessTokenErrorBody, create_access_token_error_mapper
from .create_image_collection_error import CreateImageCollectionErrorBody, create_image_collection_error_mapper
from .create_track_collection_error import CreateTrackCollectionErrorBody, create_track_collection_error_mapper
from .create_video_collection_error import CreateVideoCollectionErrorBody, create_video_collection_error_mapper
from .delete_collection_error import DeleteCollectionErrorBody, delete_collection_error_mapper
from .delete_image_collection_error import DeleteImageCollectionErrorBody, delete_image_collection_error_mapper
from .delete_image_collection_items_error import (
    DeleteImageCollectionItemsErrorBody,
    delete_image_collection_items_error_mapper,
)
from .delete_track_collection_error import DeleteTrackCollectionErrorBody, delete_track_collection_error_mapper
from .delete_track_collection_items_error import (
    DeleteTrackCollectionItemsErrorBody,
    delete_track_collection_items_error_mapper,
)
from .delete_video_collection_error import DeleteVideoCollectionErrorBody, delete_video_collection_error_mapper
from .delete_video_collection_items_error import (
    DeleteVideoCollectionItemsErrorBody,
    delete_video_collection_items_error_mapper,
)
from .download_image_error import DownloadImageErrorBody, download_image_error_mapper
from .download_sfx_error import DownloadSfxErrorBody, download_sfx_error_mapper
from .download_tracks_error import DownloadTracksErrorBody, download_tracks_error_mapper
from .download_videos_error import DownloadVideosErrorBody, download_videos_error_mapper
from .echo_error import EchoErrorBody, echo_error_mapper
from .find_similar_videos_error import FindSimilarVideosErrorBody, find_similar_videos_error_mapper
from .get_access_token_error import GetAccessTokenErrorBody, get_access_token_error_mapper
from .get_collections_error import GetCollectionsErrorBody, get_collections_error_mapper
from .get_contributor_collection_items_error import (
    GetContributorCollectionItemsErrorBody,
    get_contributor_collection_items_error_mapper,
)
from .get_contributor_collections_error import (
    GetContributorCollectionsErrorBody,
    get_contributor_collections_error_mapper,
)
from .get_contributor_collections_list_error import (
    GetContributorCollectionsListErrorBody,
    get_contributor_collections_list_error_mapper,
)
from .get_contributor_error import GetContributorErrorBody, get_contributor_error_mapper
from .get_contributor_list_error import GetContributorListErrorBody, get_contributor_list_error_mapper
from .get_editorial_categories_error import GetEditorialCategoriesErrorBody, get_editorial_categories_error_mapper
from .get_editorial_image2_error import GetEditorialImage2ErrorBody, get_editorial_image2_error_mapper
from .get_editorial_image_error import GetEditorialImageErrorBody, get_editorial_image_error_mapper
from .get_editorial_image_license_list_error import (
    GetEditorialImageLicenseListErrorBody,
    get_editorial_image_license_list_error_mapper,
)
from .get_editorial_image_livefeed_error import (
    GetEditorialImageLivefeedErrorBody,
    get_editorial_image_livefeed_error_mapper,
)
from .get_editorial_image_livefeed_items_error import (
    GetEditorialImageLivefeedItemsErrorBody,
    get_editorial_image_livefeed_items_error_mapper,
)
from .get_editorial_image_livefeed_list_error import (
    GetEditorialImageLivefeedListErrorBody,
    get_editorial_image_livefeed_list_error_mapper,
)
from .get_editorial_livefeed_error import GetEditorialLivefeedErrorBody, get_editorial_livefeed_error_mapper
from .get_editorial_livefeed_items_error import (
    GetEditorialLivefeedItemsErrorBody,
    get_editorial_livefeed_items_error_mapper,
)
from .get_editorial_livefeed_list_error import (
    GetEditorialLivefeedListErrorBody,
    get_editorial_livefeed_list_error_mapper,
)
from .get_editorial_video_error import GetEditorialVideoErrorBody, get_editorial_video_error_mapper
from .get_editorial_video_license_list_error import (
    GetEditorialVideoLicenseListErrorBody,
    get_editorial_video_license_list_error_mapper,
)
from .get_image_collection_error import GetImageCollectionErrorBody, get_image_collection_error_mapper
from .get_image_collection_items_error import GetImageCollectionItemsErrorBody, get_image_collection_items_error_mapper
from .get_image_collection_list_error import GetImageCollectionListErrorBody, get_image_collection_list_error_mapper
from .get_image_error import GetImageErrorBody, get_image_error_mapper
from .get_image_keyword_suggestions_error import (
    GetImageKeywordSuggestionsErrorBody,
    get_image_keyword_suggestions_error_mapper,
)
from .get_image_license_list_error import GetImageLicenseListErrorBody, get_image_license_list_error_mapper
from .get_image_list_error import GetImageListErrorBody, get_image_list_error_mapper
from .get_image_recommendations_error import GetImageRecommendationsErrorBody, get_image_recommendations_error_mapper
from .get_image_suggestions_error import GetImageSuggestionsErrorBody, get_image_suggestions_error_mapper
from .get_keywords_error import GetKeywordsErrorBody, get_keywords_error_mapper
from .get_sfx_details_error import GetSfxDetailsErrorBody, get_sfx_details_error_mapper
from .get_sfx_license_list_error import GetSfxLicenseListErrorBody, get_sfx_license_list_error_mapper
from .get_sfx_list_details_error import GetSfxListDetailsErrorBody, get_sfx_list_details_error_mapper
from .get_similar_images_error import GetSimilarImagesErrorBody, get_similar_images_error_mapper
from .get_similar_videos_error import GetSimilarVideosErrorBody, get_similar_videos_error_mapper
from .get_track_collection_error import GetTrackCollectionErrorBody, get_track_collection_error_mapper
from .get_track_collection_items_error import GetTrackCollectionItemsErrorBody, get_track_collection_items_error_mapper
from .get_track_collection_list_error import GetTrackCollectionListErrorBody, get_track_collection_list_error_mapper
from .get_track_error import GetTrackErrorBody, get_track_error_mapper
from .get_track_license_list_error import GetTrackLicenseListErrorBody, get_track_license_list_error_mapper
from .get_track_list_error import GetTrackListErrorBody, get_track_list_error_mapper
from .get_updated_editorial_image_error import (
    GetUpdatedEditorialImageErrorBody,
    get_updated_editorial_image_error_mapper,
)
from .get_updated_editorial_images_error import (
    GetUpdatedEditorialImagesErrorBody,
    get_updated_editorial_images_error_mapper,
)
from .get_user_error import GetUserErrorBody, get_user_error_mapper
from .get_user_subscription_list_error import GetUserSubscriptionListErrorBody, get_user_subscription_list_error_mapper
from .get_video_collection_error import GetVideoCollectionErrorBody, get_video_collection_error_mapper
from .get_video_collection_items_error import GetVideoCollectionItemsErrorBody, get_video_collection_items_error_mapper
from .get_video_collection_list_error import GetVideoCollectionListErrorBody, get_video_collection_list_error_mapper
from .get_video_error import GetVideoErrorBody, get_video_error_mapper
from .get_video_license_list_error import GetVideoLicenseListErrorBody, get_video_license_list_error_mapper
from .get_video_list_error import GetVideoListErrorBody, get_video_list_error_mapper
from .get_video_suggestions_error import GetVideoSuggestionsErrorBody, get_video_suggestions_error_mapper
from .license_editorial_image_error import LicenseEditorialImageErrorBody, license_editorial_image_error_mapper
from .license_editorial_images_error import LicenseEditorialImagesErrorBody, license_editorial_images_error_mapper
from .license_editorial_video_error import LicenseEditorialVideoErrorBody, license_editorial_video_error_mapper
from .license_images_error import LicenseImagesErrorBody, license_images_error_mapper
from .license_track_error import LicenseTrackErrorBody, license_track_error_mapper
from .license_videos_error import LicenseVideosErrorBody, license_videos_error_mapper
from .licenses_sfx_error import LicensesSfxErrorBody, licenses_sfx_error_mapper
from .list_editorial_image_categories_error import (
    ListEditorialImageCategoriesErrorBody,
    list_editorial_image_categories_error_mapper,
)
from .list_editorial_images_error import ListEditorialImagesErrorBody, list_editorial_images_error_mapper
from .list_editorial_video_categories_error import (
    ListEditorialVideoCategoriesErrorBody,
    list_editorial_video_categories_error_mapper,
)
from .list_editorial_videos_error import ListEditorialVideosErrorBody, list_editorial_videos_error_mapper
from .list_image_categories_error import ListImageCategoriesErrorBody, list_image_categories_error_mapper
from .list_similar_images_error import ListSimilarImagesErrorBody, list_similar_images_error_mapper
from .list_video_categories_error import ListVideoCategoriesErrorBody, list_video_categories_error_mapper
from .rename_image_collection_error import RenameImageCollectionErrorBody, rename_image_collection_error_mapper
from .rename_track_collection_error import RenameTrackCollectionErrorBody, rename_track_collection_error_mapper
from .rename_video_collection_error import RenameVideoCollectionErrorBody, rename_video_collection_error_mapper
from .search_catalog_error import SearchCatalogErrorBody, search_catalog_error_mapper
from .search_editorial_error import SearchEditorialErrorBody, search_editorial_error_mapper
from .search_editorial_images_error import SearchEditorialImagesErrorBody, search_editorial_images_error_mapper
from .search_editorial_videos_error import SearchEditorialVideosErrorBody, search_editorial_videos_error_mapper
from .search_images_error import SearchImagesErrorBody, search_images_error_mapper
from .search_sfx_error import SearchSfxErrorBody, search_sfx_error_mapper
from .search_tracks_error import SearchTracksErrorBody, search_tracks_error_mapper
from .search_videos_error import SearchVideosErrorBody, search_videos_error_mapper
from .upload_image_error import UploadImageErrorBody, upload_image_error_mapper
from .validate_error import ValidateErrorBody, validate_error_mapper

__all__ = [
    "AddImageCollectionItemsErrorBody",
    "AddTrackCollectionItemsErrorBody",
    "AddVideoCollectionItemsErrorBody",
    "AuthorizeErrorBody",
    "BulkSearchImagesErrorBody",
    "CreateAccessTokenErrorBody",
    "CreateImageCollectionErrorBody",
    "CreateTrackCollectionErrorBody",
    "CreateVideoCollectionErrorBody",
    "DeleteCollectionErrorBody",
    "DeleteImageCollectionErrorBody",
    "DeleteImageCollectionItemsErrorBody",
    "DeleteTrackCollectionErrorBody",
    "DeleteTrackCollectionItemsErrorBody",
    "DeleteVideoCollectionErrorBody",
    "DeleteVideoCollectionItemsErrorBody",
    "DownloadImageErrorBody",
    "DownloadSfxErrorBody",
    "DownloadTracksErrorBody",
    "DownloadVideosErrorBody",
    "EchoErrorBody",
    "FindSimilarVideosErrorBody",
    "GetAccessTokenErrorBody",
    "GetCollectionsErrorBody",
    "GetContributorCollectionItemsErrorBody",
    "GetContributorCollectionsErrorBody",
    "GetContributorCollectionsListErrorBody",
    "GetContributorErrorBody",
    "GetContributorListErrorBody",
    "GetEditorialCategoriesErrorBody",
    "GetEditorialImage2ErrorBody",
    "GetEditorialImageErrorBody",
    "GetEditorialImageLicenseListErrorBody",
    "GetEditorialImageLivefeedErrorBody",
    "GetEditorialImageLivefeedItemsErrorBody",
    "GetEditorialImageLivefeedListErrorBody",
    "GetEditorialLivefeedErrorBody",
    "GetEditorialLivefeedItemsErrorBody",
    "GetEditorialLivefeedListErrorBody",
    "GetEditorialVideoErrorBody",
    "GetEditorialVideoLicenseListErrorBody",
    "GetImageCollectionErrorBody",
    "GetImageCollectionItemsErrorBody",
    "GetImageCollectionListErrorBody",
    "GetImageErrorBody",
    "GetImageKeywordSuggestionsErrorBody",
    "GetImageLicenseListErrorBody",
    "GetImageListErrorBody",
    "GetImageRecommendationsErrorBody",
    "GetImageSuggestionsErrorBody",
    "GetKeywordsErrorBody",
    "GetSfxDetailsErrorBody",
    "GetSfxLicenseListErrorBody",
    "GetSfxListDetailsErrorBody",
    "GetSimilarImagesErrorBody",
    "GetSimilarVideosErrorBody",
    "GetTrackCollectionErrorBody",
    "GetTrackCollectionItemsErrorBody",
    "GetTrackCollectionListErrorBody",
    "GetTrackErrorBody",
    "GetTrackLicenseListErrorBody",
    "GetTrackListErrorBody",
    "GetUpdatedEditorialImageErrorBody",
    "GetUpdatedEditorialImagesErrorBody",
    "GetUserErrorBody",
    "GetUserSubscriptionListErrorBody",
    "GetVideoCollectionErrorBody",
    "GetVideoCollectionItemsErrorBody",
    "GetVideoCollectionListErrorBody",
    "GetVideoErrorBody",
    "GetVideoLicenseListErrorBody",
    "GetVideoListErrorBody",
    "GetVideoSuggestionsErrorBody",
    "LicenseEditorialImageErrorBody",
    "LicenseEditorialImagesErrorBody",
    "LicenseEditorialVideoErrorBody",
    "LicenseImagesErrorBody",
    "LicenseTrackErrorBody",
    "LicenseVideosErrorBody",
    "LicensesSfxErrorBody",
    "ListEditorialImageCategoriesErrorBody",
    "ListEditorialImagesErrorBody",
    "ListEditorialVideoCategoriesErrorBody",
    "ListEditorialVideosErrorBody",
    "ListImageCategoriesErrorBody",
    "ListSimilarImagesErrorBody",
    "ListVideoCategoriesErrorBody",
    "RenameImageCollectionErrorBody",
    "RenameTrackCollectionErrorBody",
    "RenameVideoCollectionErrorBody",
    "SearchCatalogErrorBody",
    "SearchEditorialErrorBody",
    "SearchEditorialImagesErrorBody",
    "SearchEditorialVideosErrorBody",
    "SearchImagesErrorBody",
    "SearchSfxErrorBody",
    "SearchTracksErrorBody",
    "SearchVideosErrorBody",
    "UploadImageErrorBody",
    "ValidateErrorBody",
    "add_image_collection_items_error_mapper",
    "add_track_collection_items_error_mapper",
    "add_video_collection_items_error_mapper",
    "authorize_error_mapper",
    "bulk_search_images_error_mapper",
    "create_access_token_error_mapper",
    "create_image_collection_error_mapper",
    "create_track_collection_error_mapper",
    "create_video_collection_error_mapper",
    "delete_collection_error_mapper",
    "delete_image_collection_error_mapper",
    "delete_image_collection_items_error_mapper",
    "delete_track_collection_error_mapper",
    "delete_track_collection_items_error_mapper",
    "delete_video_collection_error_mapper",
    "delete_video_collection_items_error_mapper",
    "download_image_error_mapper",
    "download_sfx_error_mapper",
    "download_tracks_error_mapper",
    "download_videos_error_mapper",
    "echo_error_mapper",
    "find_similar_videos_error_mapper",
    "get_access_token_error_mapper",
    "get_collections_error_mapper",
    "get_contributor_collection_items_error_mapper",
    "get_contributor_collections_error_mapper",
    "get_contributor_collections_list_error_mapper",
    "get_contributor_error_mapper",
    "get_contributor_list_error_mapper",
    "get_editorial_categories_error_mapper",
    "get_editorial_image2_error_mapper",
    "get_editorial_image_error_mapper",
    "get_editorial_image_license_list_error_mapper",
    "get_editorial_image_livefeed_error_mapper",
    "get_editorial_image_livefeed_items_error_mapper",
    "get_editorial_image_livefeed_list_error_mapper",
    "get_editorial_livefeed_error_mapper",
    "get_editorial_livefeed_items_error_mapper",
    "get_editorial_livefeed_list_error_mapper",
    "get_editorial_video_error_mapper",
    "get_editorial_video_license_list_error_mapper",
    "get_image_collection_error_mapper",
    "get_image_collection_items_error_mapper",
    "get_image_collection_list_error_mapper",
    "get_image_error_mapper",
    "get_image_keyword_suggestions_error_mapper",
    "get_image_license_list_error_mapper",
    "get_image_list_error_mapper",
    "get_image_recommendations_error_mapper",
    "get_image_suggestions_error_mapper",
    "get_keywords_error_mapper",
    "get_sfx_details_error_mapper",
    "get_sfx_license_list_error_mapper",
    "get_sfx_list_details_error_mapper",
    "get_similar_images_error_mapper",
    "get_similar_videos_error_mapper",
    "get_track_collection_error_mapper",
    "get_track_collection_items_error_mapper",
    "get_track_collection_list_error_mapper",
    "get_track_error_mapper",
    "get_track_license_list_error_mapper",
    "get_track_list_error_mapper",
    "get_updated_editorial_image_error_mapper",
    "get_updated_editorial_images_error_mapper",
    "get_user_error_mapper",
    "get_user_subscription_list_error_mapper",
    "get_video_collection_error_mapper",
    "get_video_collection_items_error_mapper",
    "get_video_collection_list_error_mapper",
    "get_video_error_mapper",
    "get_video_license_list_error_mapper",
    "get_video_list_error_mapper",
    "get_video_suggestions_error_mapper",
    "license_editorial_image_error_mapper",
    "license_editorial_images_error_mapper",
    "license_editorial_video_error_mapper",
    "license_images_error_mapper",
    "license_track_error_mapper",
    "license_videos_error_mapper",
    "licenses_sfx_error_mapper",
    "list_editorial_image_categories_error_mapper",
    "list_editorial_images_error_mapper",
    "list_editorial_video_categories_error_mapper",
    "list_editorial_videos_error_mapper",
    "list_image_categories_error_mapper",
    "list_similar_images_error_mapper",
    "list_video_categories_error_mapper",
    "rename_image_collection_error_mapper",
    "rename_track_collection_error_mapper",
    "rename_video_collection_error_mapper",
    "search_catalog_error_mapper",
    "search_editorial_error_mapper",
    "search_editorial_images_error_mapper",
    "search_editorial_videos_error_mapper",
    "search_images_error_mapper",
    "search_sfx_error_mapper",
    "search_tracks_error_mapper",
    "search_videos_error_mapper",
    "upload_image_error_mapper",
    "validate_error_mapper",
]
