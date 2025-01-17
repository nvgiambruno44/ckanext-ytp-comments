import logging
from pylons.i18n import _

from ckan import logic
import ckanext.ytp.comments.model as comment_model

log = logging.getLogger(__name__)

def comment_delete(context, data_dict):
    model = context['model']
    user = context['user']
    userobj = model.User.get(user)
    cid = logic.get_or_bust(data_dict, 'id')

    comment = comment_model.Comment.get(cid)
    if not comment:
        return {'success': False, 'msg': _('Comment does not exist')}

    if comment.user_id is not userobj.id:
        return {'success': False, 'msg': _('User is not the author of the comment')}

    return {'success': True}
