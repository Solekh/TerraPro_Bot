from bot.dispacher import dp
from bot.handlers.additional_handlers import extra_router
from bot.handlers.main_handler import main_router
from bot.handlers.backup import routine

dp.include_routers(*[
    main_router,
    routine,
    extra_router,
])
