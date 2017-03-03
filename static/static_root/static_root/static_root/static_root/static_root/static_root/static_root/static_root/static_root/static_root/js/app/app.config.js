'use strict' ;

    angular.module('app')
    .config(function(
            $locationProvider,
            $routeProvider
            ){

            $locationProvider.html5Mode({
                enabled:true})

            $routeProvider.
                when('/',{
                    template: "<blog-list></blog-list>"
                }).
                when('/about',{
                    templateUrl: '/api/templates/about.html'
                }).
                when('/project',{
                    template: "<blog-list></blog-list>"
                }).
                when('/project/:slug/',{
                    template: "<blog-detail></blog-detail>"
                }).
                otherwise({
                    template : "Not Found"
                })

    });