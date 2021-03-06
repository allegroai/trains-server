from jsonmodels import models, fields

from apiserver.apimodels import ListField, ActualEnumField
from apiserver.apimodels.organization import TagsRequest
from apiserver.database.model import EntityVisibility


class ProjectReq(models.Base):
    project = fields.StringField()


class GetHyperParamReq(ProjectReq):
    page = fields.IntField(default=0)
    page_size = fields.IntField(default=500)


class ProjectTagsRequest(TagsRequest):
    projects = ListField(str)


class ProjectTaskParentsRequest(ProjectReq):
    projects = ListField(str)
    tasks_state = ActualEnumField(EntityVisibility)

