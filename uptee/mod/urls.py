from django.conf.urls import *

urlpatterns = patterns('mod.views',
    url(r'^servers/$', 'server_list', name='server_list'),
    url(r'^servers/type:(?P<server_status>online|offline)$', 'server_list', name='server_list__type'),
    url(r'^servers/(?P<username>[\w.@+-]+)/$', 'server_list', name='user_server_list'),
    url(r'^servers/(?P<username>[\w.@+-]+)/type:(?P<server_status>online|offline)$', 'server_list', name='user_server_list__type'),
    url(r'^server/(?P<server_id>\d+)/$', 'server_detail', name='server_detail'),
    url(r'^server/(?P<server_id>\d+)/editsettings/$', 'server_edit', name='server_edit'),
    url(r'^server/(?P<server_id>\d+)/uploadmap/$', 'upload_map', name='upload_map'),
    url(r'^server/(?P<server_id>\d+)/editvotes/$', 'server_edit_votes', name='server_edit_votes'),
    url(r'^server/(?P<server_id>\d+)/editrconcommands/$', 'server_edit_rcon_commands', name='server_edit_rcon_commands'),
    url(r'^server/(?P<server_id>\d+)/edittunings/$', 'server_tunes', name='server_tunes'),
    url(r'^server/(?P<server_id>\d+)/changemod/$', 'server_change_mod', name='server_change_mod'),
    url(r'^server/(?P<server_id>\d+)/showvotes/$', 'server_votes', name='server_votes'),
    url(r'^server/(?P<server_id>\d+)/editserverdescription/$', 'server_edit_description', name='server_edit_description'),
    url(r'^server/(?P<server_id>\d+)/moderators/$', 'server_moderators', name='server_moderators'),
    url(r'^server/(?P<server_id>\d+)/moderators/(?P<user_id>\d+)/$', 'server_edit_moderator', name='server_edit_moderator'),
    url(r'^server/(?P<server_id>\d+)/console/$', 'server_console', name='server_console'),
    url(r'^server/(?P<server_id>\d+)/downloadconfig/$', 'config_download', name='config_download'),
    url(r'^server/(?P<server_id>\d+)/events/$', 'events_ajax', name='events_ajax'),
    url(r'^server/(?P<server_id>\d+)/events/add/$', 'events_add_ajax', name='events_add_ajax'),
    url(r'^server/(?P<server_id>\d+)/events/delete/$', 'events_delete_ajax', name='events_delete_ajax'),
    url(r'^startstopserver/(?P<server_id>\d+)/$', 'start_stop_server', name='start_stop_server'),
    url(r'^updatesettings/(?P<server_id>\d+)/$', 'update_settings', name='update_settings'),
    url(r'^updatevotes/(?P<server_id>\d+)/$', 'update_votes', name='update_votes'),
    url(r'^updaterconcommands/(?P<server_id>\d+)/$', 'update_rcon_commands', name='update_rcon_commands'),
    url(r'^updatetunings/(?P<server_id>\d+)/$', 'update_tunes', name='update_tunes'),
    url(r'^server_info_update/(?P<server_id>\d+)/$', 'server_info_update_ajax', name='server_info_update_ajax'),
    url(r'^server_terminal_command/(?P<server_id>\d+)/$', 'terminal_command_ajax', name='terminal_command_ajax'),
    url(r'^server_terminal_receive/(?P<server_id>\d+)/$', 'terminal_receive_ajax', name='terminal_receive_ajax'),
    url(r'^map/(?P<map_id>\d+)/$', 'map_details', name='map_details'),
    url(r'^map/(?P<map_id>\d+)/download/$', 'map_download', name='map_download'),
    url(r'^map/(?P<map_id>\d+)/delete/$', 'delete_map', name='delete_map')
)
