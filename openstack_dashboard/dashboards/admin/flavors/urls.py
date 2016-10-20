# Copyright 2012 United States Government as represented by the
# Administrator of the National Aeronautics and Space Administration.
# All Rights Reserved.
#
# Copyright 2012 Nebula, Inc.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from django.conf import settings
from django.conf.urls import url

from openstack_dashboard.dashboards.admin.flavors import views


if settings.ANGULAR_FEATURES['flavors_panel']:
    # New angular panel
    urlpatterns = [
        url(r'^$', views.AngularIndexView.as_view(), name='index'),
        url(r'^create/$', views.AngularIndexView.as_view(), name='create'),
        url(r'^(?P<id>[^/]+)/update/$', views.AngularIndexView.as_view(),
            name='index'),
    ]
else:
    urlpatterns = [
        url(r'^$', views.IndexView.as_view(), name='index'),
        url(r'^create/$', views.CreateView.as_view(), name='create'),
        url(r'^(?P<id>[^/]+)/update/$',
            views.UpdateView.as_view(), name='update'),
    ]
