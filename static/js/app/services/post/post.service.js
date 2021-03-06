'use strict';

angular.
    module('post').
        factory('Post', function($resource){
            var url = '/api/posts/:slug/'
            return $resource(url, {}, {
                query: {
                    method: "GET",
                    params: {},
                    isArray: true,
                    cache: false,
                    transformResponse: function(data, headersGetter, status){
                        // console.log(data)
                        return data
                    }
                    // interceptor
                },
                get: {
                    method: "GET",
                    params: {"slug": "@slug"},
                    isArray: false,
                    cache: false,
                }
            })

        });