// use a closure to allow attaching the mapping of values directly to
// the function, a bit cleaner
fv_author_pays = (function(resultobj) {
    var that = function(resultobj) {
        if(that.mapping[resultobj['bibjson']['author_pays']]) {
            var result = '<span class=' + that.mapping[resultobj['bibjson']['author_pays']]['class'] + '>';
            result += that.mapping[resultobj['bibjson']['author_pays']]['text'];
            result += '</span>';
            return result;
        } else {
            return resultobj['bibjson']['author_pays'];
        }
    };
    return that;
})();

fv_author_pays.mapping = {
    "Y": {"text": "Has charges", "class": "red"},
    "N": {"text": "No charges", "class": "green"},
    "CON": {"text": "Conditional charges", "class": "blue"},
    "NY": {"text": "No info available", "class": ""},
}

fv_created_date = (function (resultobj) {
    var that = function(resultobj) {
        return iso_datetime2date(resultobj['created_date']);
    };
    return that;
})();


fv_abstract = (function (resultobj) {
    var that = function(resultobj) {
        if (resultobj['bibjson']['abstract']) {
            var result = '<a class="abstract_action" href="" rel="';
            result += resultobj['id'];
            result += '">(expand)</a> <span class="abstract_text" rel="';
            result += resultobj['id'];
            result += '">' + '<br>';
            result += resultobj['bibjson']['abstract'];
            result += '</span>';
            return result;
        }
        return false;
    };
    return that;
})();


fv_addthis = (function (resultobj) {
    var that = function(resultobj) {
        var result = '<a class="addthis_button"';
        result += ' addthis:title="' + resultobj['bibjson']['title'] + '"';
        var query = '{"query":{"query_string":{"query":"' + resultobj['id'] + '"}}}';
        result += ' addthis:url="http://' + document.domain + '/search?source=' + escape(query) + '"';
        result += ' href="http://www.addthis.com/bookmark.php?v=300&amp;pubid=ra-52ae52c34c6f0a3e"><img src="http://s7.addthis.com/static/btn/v2/lg-share-en.gif" width="125" height="16" alt="Bookmark and Share" style="border:0"/></a>';
        return result;
    };
    return that;
})();

fv_journal_license = (function (resultobj) {
    var that = function(resultobj) {
        if (resultobj.bibjson && resultobj.bibjson.journal && resultobj.bibjson.journal.license) {
            var lics = resultobj["bibjson"]["journal"]["license"]
            if (lics.length > 0) {
                return lics[0].title
            }
        }
        else if (resultobj.bibjson && resultobj.bibjson.license) {
            var lics = resultobj["bibjson"]["license"]
            if (lics.length > 0) {
                return lics[0].title
            }
        }
        
        return false;
    };
    return that;
})();

fv_type_icon = (function (resultobj) {
    var that = function(resultobj) {
        if (resultobj.bibjson && resultobj.bibjson.journal) {
            // this is an article
            return "<i class='icon icon-file'></i>"
        }
        else {
            // this is a journal
            return "<i class='icon icon-book'></i>"
        }
    };
    return that;
})();

fv_title_field = (function (resultobj) {
    var that = function(resultobj) {
        var field = '<span class="title">'
        if (resultobj.bibjson && resultobj.bibjson.journal) {
            // this is an article
            field += "<i class='icon icon-file'></i> "
        }
        else {
            // this is a journal
            field += "<i class='icon icon-book'></i> "
        }
        if (resultobj.bibjson.title) {
            field += resultobj.bibjson.title + "</span>"
            return field
        } else {
            return false
        }
    };
    return that;
})();
