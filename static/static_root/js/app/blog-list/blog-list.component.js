'use strict';

angular.module('blogList').
    component('blogList', {
        templateUrl: '/api/templates/blog_list.html',
        controller: function(Post, $location, $routeParams, $rootScope, $scope){
            // console.log($location.search())
            Post.query(function(data){
                $scope.items=data;
            })
        }

});