from django.urls import path
from . import views
from blogging import settings
from django.conf.urls.static import static

urlpatterns=[
    path('',views.home),
    path('signup/',views.signup),
    path('registering/',views.registering),
    path('verify/',views.verify),
    path('login/',views.login),
    path('viewprofile/',views.viewprofile),
    path('editprofile/',views.editprofile),
    path('editing/',views.editing),
    path('logout/',views.logout),
    path('changing/',views.changing),
    path('changepass/',views.changepass),
    path('myadmin/',views.myadmin),
    path('forgotpassword/',views.forgotpass),
    path('admin_verify/',views.admin_verify),
    path('updatinga/',views.updatinga),
    path('viewinga/',views.viewinga),
    path('update/',views.update),
    path('deletinga/',views.deletinga),
    path('addpost/',views.addpost),
    path('viewposts/',views.viewposts),
    path('addingimage/',views.addingimage),
    path('commenting/',views.commenting),
    path('liking/',views.liking),
    path('bookmarking/',views.bookmarking),
    path('likes/',views.likes),
    path('comments/',views.comments),
    path('bookmarks/',views.bookmarks),
    path('editpost/',views.editpost),
    path('deletepost/',views.deletepost),
    path('editingpost/',views.editingpost),
    path('viewadmin/',views.viewadmin),
    path('removebookmark/',views.removebookmark),
    path('unliking/',views.unliking),
    path('unbookmarking/',views.unbookmarking),
    path('notify/',views.notify),
    path('removeDp/',views.removeDp),
    path('profile/',views.profile),
    path('verifypass/',views.verifypass),
    path('reset/',views.reset),
    path('verifying/',views.verifying),
    path('about/',views.about),
]

if settings.DEBUG: 
        urlpatterns += static(settings.MEDIA_URL, 
                              document_root=settings.MEDIA_ROOT)