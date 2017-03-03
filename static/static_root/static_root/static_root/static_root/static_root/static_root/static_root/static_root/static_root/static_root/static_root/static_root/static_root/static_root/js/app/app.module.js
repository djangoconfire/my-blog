'use strict' ;

    angular.module('app',
    [
        //external
        'angularUtils.directives.dirPagination',
        'ngResource',
        'ngRoute',
        'ui.bootstrap',

        //Internal
        'blogList',
        'blogDetail',
        'post'
    ]);