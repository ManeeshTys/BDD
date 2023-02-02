from behave import *
@given(u'I launch browser')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given I launch browser')


@when(u'I open Application')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I open Application')


@when(u'Enter valid username and password')
def step_impl(context):
    raise NotImplementedError(u'STEP: When Enter valid username and password')


@when(u'click on login')
def step_impl(context):
    raise NotImplementedError(u'STEP: When click on login')


@then(u'user must successfully see the dashboard')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then user must successfully see the dashboard')


@when(u'Navigate to search page')
def step_impl(context):
    raise NotImplementedError(u'STEP: When Navigate to search page')


@then(u'search page should display')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then search page should display')


@when(u'navigate to advanced search page')
def step_impl(context):
    raise NotImplementedError(u'STEP: When navigate to advanced search page')


@then(u'advance search page should display')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then advance search page should display')