function customise_facetview_init() {
    insert_progress_bar();
}

function customise_facetview_results() {
    //$('#facetview_filters .table-striped tbody tr:nth-child(2n+1) td, .table-striped tbody tr:nth-child(2n+1) th').css('background-color', '#ffeece');
    $('.facetview_filtershow').bind('click', toggle_bottom_border);
    $('.facetview_orderby').css('background-color', 'white');
    $('.facetview_orderby').css('width', 'auto');
    $('.facetview_searchfield').css('width', 'auto');
    $('.facetview_metadata div').css('border-color', '#F68B1F');
    $('.facetview_decrement, .facetview_increment').css('color', '#F68B1F');
    $('.date-month').each(expand_month)
}

function toggle_bottom_border() {
    which_facet = this.rel;
    theanchor = $(this);
    if ( theanchor.hasClass('facetview_open') ) {
       $('#facetview_' + which_facet).addClass('no-bottom');
    } else {
       $('#facetview_' + which_facet).removeClass('no-bottom');
    }
}

months_english = {
    '1': 'January',
    '2': 'February',
    '3': 'March',
    '4': 'April',
    '5': 'May',
    '6': 'June',
    '7': 'July',
    '8': 'August',
    '9': 'September',
    '10': 'October',
    '11': 'November',
    '12': 'December'
}

function expand_month() {
    this.innerHTML = months_english[this.innerHTML];
}

function insert_progress_bar() {
        $('#facetview_selectedfilters').append('<div class="progress progress-danger progress-striped active notify-loading" id="search-progress-bar"><div class="bar"></div></div>');
}