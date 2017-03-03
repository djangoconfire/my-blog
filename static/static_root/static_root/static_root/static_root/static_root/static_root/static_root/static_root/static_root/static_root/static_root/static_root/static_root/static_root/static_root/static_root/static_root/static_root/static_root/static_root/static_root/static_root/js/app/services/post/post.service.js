'use strict';

    angular.module('post')
    .factory('Post',function($resource){
        var url='/api/posts/:slug'
        return $resource(url,{
                slug: '@slug'

                });



    });